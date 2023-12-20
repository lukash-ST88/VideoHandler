from ffmpeg import FFmpeg


def handle_video(input_video, output_video):
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input(input_video)
        .output(
            f"HandledVideo/{output_video}.mp4",
            {"codec:v": "libx264"},
            vf="scale=1280:-1",
            preset="veryslow",
            crf=24,
        )
    )

    ffmpeg.execute()

