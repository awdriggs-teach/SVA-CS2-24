# Command Line Tools for Artists

Here are three useful tools and some tips on getting started.

[ImageMagick](#Imagemagick) - command line image manipulation
[FFmpeg](#FFmpeg) - everything audio/video related 
[Youtube DL](#youtube-dl) - streaming video extractor! 

If you get stuck with something, you can always look at the help manual for any command using the `-f` flag.
For example, `ffmpeg -h`, will show you the options when running the ffmpeg command. 

# Imagemagick
Imagemagick is a powerful command line image editor that can do a lot of the functions that you probably use Photoshop for.

## Installation
On a mac, type `brew install imagemagick`

On windows, use the binary to install: [Imagemagick - Windows Binary Release](https://imagemagick.org/script/download.php#windows) 

## Anatomy of a Command
`convert inputName.ext -some_command options outputName.ext`

On Windows, use `magick` to run a command instead of convert

## Useful Commands

### Convert Filetypes
- `convert file.jpg file.png` - convert a single jpg to a png, changing the output name will change the file name
- `convert '*.jpg' -set filename:out "%[basename]" '%[filename:out].png'` - convert all jpg  to pngs

### Gif Magick!
- `convert *.jpg -loop 0 test.gif` - creates a gif from any jpeg that is in a folder

### Resize and convert!
- `convert input.jpg -resize 900x900 test.png` - larger dimension resized to 900px, the small dimension is auto scaled, aspect ratio is maintained 
- `convert input.jpg -resize 900 test.png` - set width, auto set height, aspect ratio is maintained
- `convert input.jpg -resize x900 test.png` - set height, auto set width, aspect ratio is maintained    
- `convert input.jpg -resize 200% test.png` - both dimensions scaled by 200%, aspect ratio is maintained
- `convert input.jpg -resize 200x50% test.png` - width is scaled by 200%, height is scaled to 50%, aspect ratio is lost. 
- `convert '*.jpg' -resize 200 -set filename:out '%[basename]' './thumbs/thumbs-%[filename:out].png'` - resize all images to 200px width, save to a folder 'thumbs' with a new filename thumbs + original filename.

### Trim and Crop
- `convert image.jpg -crop 200x200` - creates 200px by 200px tiles of any image automatically
- `convert image.jpg -crop 200x200+100+200 cropped.jpg` - creates a single image, 200px by 200px, 100 is the x offset and 200 the y offset 
- `convert image.jpg -trim new.jpg` - auto crop! Removes any unwanted empty space around an image.

## Batch with mogrify
**Warning, mogrify overwrites file by default! Can do permanent damage if you don't have it write to a new file!**
- `mogrify -format jpg  *.png` - This is safe! Changes all png files to jpg, writes new files perserving originals
- `mogrify -resize 20x20 *.jpg` - Danger! Overwrites all images resized to 20 by 20px.

### Resources
- [Commands](https://imagemagick.org/script/command-line-processing.php)
- [Mogrify](https://imagemagick.org/script/mogrify.php) - inline batch processing
- [Example Gallery](https://imagemagick.org/script/examples.php)
               
# FFmpeg
[FFmpeg](https://www.ffmpeg.org) is a command line tool for audio/video. It is used a lot in other conversion tools.  

## Installation
On a mac, type ` brew install ffmpeg`

On a PC, use this link to download an build from source. [link](https://ffmpeg.org/download.html)

## Anatomy of a Command 
`ffmpeg -i input.xyz options output.xyz`

## Useful Commands 

### Convert between Formats and Codecs 
`ffmpeg -i input.xyz output.xyz`

See the list of formats + codecs:
- `ffmpeg -formats` 
- ` ffmpeg -codecs`
- `ffmpeg -i myfile.mp4 -vcodec libx265 myfile_265.mp4` - applies a specific codec when converting

### Movie to GIF
`ffmpeg -i input.mp4 -f gif output.gif` - convert a movie file to a gif 
 
You can lower the frame rate by adding `-r 10` changing the frame rate to 10. Similarly, adding `-r 320x240` will change the image size.

Too Big? Try using imagemagick to optimize the gif `convert -layers Optimize output.gif output_optimized.gif` 

### Trim
`ffmpeg -ss 10 -i input.mp4 -c copy -t 15 output.mp4` - trim a video without re-encoding

Explainer:
- `ffmpeg` - launches FFmpeg
- `-ss ##` - start from __ in sec
- `-i input.mp4` - input file
- `-c copy` - use existing codec (instant, no re-encoding)
- `-t ##` - duration for new clip in sec (use `-to ##` for time in clip)
- `output.mp4` - name/path for new output file

### Extract frames
Use the `-vf` flag to output video frames.

Make a directory for the frames `mkdir frames`

Set input file, frames per second for output, file path/type:
`ffmpeg -i input.mp4 -vf fps=1 frames/out_%04d.png`

Explainer:
- `-vf fps=1` exports # frames per second
- `%04d` specify how you want the frames to be numbered, this uses 4 padded digits (0000, 0001, ...)

### Extract Audio
`ffmpeg -i in.mp4 -vn -ac 2 out.mp3` - Extract audio and convert to mp3 (or other format):  

### Merge Audio + Video
Merge an audio and  video, uses the shortest one as the file length
`ffmpeg -i input.mov -i input.mp3 -c:v copy -map 0:v:0 -map 1:a:0 -shortest output.mov`

### Video from directory
Create a movie from a directory of images!
` ffmpeg -framerate 30 -pattern_type glob -i '*.png' \
-c:v libx264 -pix_fmt yuv420p out.mp4`

Explainer: 
* `-framerate 30` sets number of frames per second
* `*.png` searches for PNGs (or use `*.jpg`)

### Speed
Useful to speed up long screen-recordings:
`ffmpeg -i input.mp4 -filter:v "setpts=0.5*PTS" output.mp4`

Explainer:
* `-filter:v "setpts=0.5*PTS"` 0.5 = faster, 1.0 = normal, 1.5 = slower

### Playback
FFmpeg ships with a minimal audio/video player `ffplay` that you can launch from the terminal.  
`ffplay input.mp4`

Useful shortcuts:  
- `q`/`ESC` (quit)  
- `f` (toggle fullscreen)  
- `p` / `SPACEBAR` (toggle pause)  
- `m` (toggle mute)  
- `left/right` (seek backward/forward 10 seconds)  
- `up/down` (seek backward/forward 1 minute)

Loop endless at fullscreen:
`ffplay -fs -loop 0 *input.mp4`

View audio waveform:
`ffplay -showmode 1 *input.mp4`

View audio frequency (FFT) spectrogram:
`ffplay -showmode 2 input.mp4`

View debug [Motion Vectors](https://trac.ffmpeg.org/wiki/Debug/MacroblocksAndMotionVectors):
`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb input.mp4`

Export Motion Vectors only:
`ffmpeg -flags2 +export_mvs -i input.mp4 -vf "split[src],codecview=mv=pf+bf+bb[vex],[vex][src]blend=all_mode=difference128,eq=contrast=7:brightness=-1:gamma=1.5" -c:v libx264 output.mp4`

### Additional Links
- [FFmpeg CLI guide](https://www.ffmpeg.org/ffmpeg.html)
- [Rick Companje - FFMpeg Tips](https://companje.nl/ffmpeg)
- [Complete list of ffmpeg flags / commands](https://gist.github.com/tayvano/6e2d456a9897f55025e25035478a3a50)
- [Werner Robitza FFmpeg guide](http://slhck.info/ffmpeg-encoding-course/#/20)
- [20 FFmpeg commands for beginners](https://www.ostechnix.com/20-ffmpeg-commands-beginners/)
- [Fancy (ffplay) Filtering Examples](https://trac.ffmpeg.org/wiki/FancyFilteringExamples)
- [More tips for converting images to video](http://hamelot.io/visualization/using-ffmpeg-to-convert-a-set-of-images-into-a-video/)
- [Ludwig Zeller FFmpeg Cheatsheet](https://gitlab.fhnw.ch/hgk-ml/hgk-ml-tools/tree/master/ffmpeg_cheatsheet)
- [Giphy Engineering FFmpeg Guide](https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/)

# youtube-dl
[youtube-dl](https://ytdl-org.github.io/youtube-dl/index.html) is an online media extractor.  
The ultimate tool for downloading and archiving media files from *[almost any](https://ytdl-org.github.io/youtube-dl/supportedsites.html)* website.  
Lately, there's been more activity and updates on a fork, [youtube-dlp](https://github.com/yt-dlp/yt-dlp), so might be better to use this one.

## Install
On a mac, type `brew install yt-dlp` for the forked version that works with more sites and has more options.

For Windows, download the .exe from [here](https://github.com/yt-dlp/yt-dlp#installation)

## Anatomy of a command 
`cd` into the directory where you want to save the video. 

`yt-dlp *some url*`*

### Formats
Most hosted videos have multiple files to stream depending on connection speed / quality.

List formats:
`yt-dlp *VIDEO_URL* -F`

It will return a long list of available formats, starting with an ID.  
Then download the one you prefer:
`yt-dlp *VIDEO_URL* -f ##`

Or download the *best* mp4 or similar format:
`yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best' *VIDEO_URL*`

Or download the *best* m4a or audio format:
`yt-dlp -f 'bestaudio[ext=m4a]' *VIDEO_URL*`

After using yt-dlp you can use ffmpeg to trim video, make it a gif, or perform other tasks!

### Additional Links
- [yt-dlp options](https://github.com/yt-dlp/yt-dlp#usage-and-options), laundry list of features to use
- [youtube-dlg](https://github.com/oleksis/youtube-dl-gui), a GUI approach for yt-dl(p)
