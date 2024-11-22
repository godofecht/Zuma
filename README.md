# Zuma - Sequence Merging Software for Folder Directories

Zuma is a lightweight, standalone application designed to merge video files from gaming sessions captured by software like Outplayed. Each gaming session outputs multiple video files in separate folders, making it cumbersome to manage and review these clips. Zuma solves this problem by efficiently combining all video files within a directory into a single, continuous video.

## Features:
- **Automatic Merging:** Combines all video files in a specified directory into one continuous video with minimal user intervention.
- **Simple to Use:** Just copy the executable to the desired folder, and with a single command, your video files are merged into a single output.
- **Output File:** The merged video is saved as `combined.mp4` in the same directory.

## How To Use Zuma:

1. **Prepare the Directory:**
   - Move or copy all video files you wish to combine into a single directory. Ensure this directory contains only the video files to be merged.

2. **Run Zuma:**
   - Open a terminal and navigate to the directory containing your video files and `zuma.exe`.
   - Run the following command to start the merging process:
     ```bash
     ./zuma.exe
     ```
   - The software will automatically process the files and create a single output video named `combined.mp4` in the same directory.

## Important Notes:
- **File Renaming:** Zuma will rename your video files during the merging process. We are currently working on a solution to prevent this.
- **Requirements:** Zuma uses the `Avel` FFmpeg wrapper for Python to handle the video processing. You can find more about `Avel` on its [GitHub repository](https://github.com/evliang/avel).
