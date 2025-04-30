import av
import os

def encode_video(input_file, output_file, codec='hevc', crf=None, gop_size=15, b_frames=0):
    """Optimized HEVC encoding (on-the-fly)."""
    
    input_container = av.open(input_file)
    output_container = av.open(output_file, mode='w')

    input_stream = next(s for s in input_container.streams if s.type == 'video')
    frame_rate = int(input_stream.average_rate)

    output_stream = output_container.add_stream(codec, rate=frame_rate)
    output_stream.width = input_stream.codec_context.width
    output_stream.height = input_stream.codec_context.height
    output_stream.pix_fmt = 'yuv420p'
    output_stream.gop_size = gop_size
    output_stream.options = {
        'crf': str(crf),  
        'bf': str(b_frames),
    }

    for i, frame in enumerate(input_container.decode(video=0)):
        if i % gop_size == 0:
            frame.pict_type = av.video.frame.PictureType.I  
        elif b_frames > 0 and i % 2 == 0:
            frame.pict_type = av.video.frame.PictureType.B  
        else:
            frame.pict_type = av.video.frame.PictureType.P  

        for packet in output_stream.encode(frame):
            output_container.mux(packet)

    for packet in output_stream.encode():
        output_container.mux(packet)

    output_container.close()
    input_container.close()

# Define input video
input_file = "D:\\Arani Sir IP\\dataset_town5.mp4" # Replace with your actual video file

# List of CRF values to test
crf_values = [18, 23, 28, 35, 40]
gop_size = 15  # GOP size as per your requirement

# Create output directory
output_dir = "D:\Arani Sir IP\\town_5\\H.265\\only I-frames"
os.makedirs(output_dir, exist_ok=True)

# 🚀 (i) Only I-frames
for crf in crf_values:
    output_file = os.path.join(output_dir, f"output_I_frames_crf_{crf}.mp4")
    print(f"Encoding {output_file}...")
    encode_video(input_file, output_file, crf=crf, gop_size=1, b_frames=0)

# 🚀 (ii) One I-frame per GOP, rest P-frames
for crf in crf_values:
    output_file = os.path.join(output_dir, f"output_I_P_frames_crf_{crf}.mp4")
    print(f"Encoding {output_file}...")
    encode_video(input_file, output_file, crf=crf, gop_size=gop_size, b_frames=0)

# 🚀 (iii) One I-frame per GOP, interleaved P and B-frames
for crf in crf_values:
    output_file = os.path.join(output_dir, f"output_I_P_B_frames_crf_{crf}.mp4")
    print(f"Encoding {output_file}...")
    encode_video(input_file, output_file, crf=crf, gop_size=gop_size, b_frames=1)

print("✅ Encoding complete! All files saved in 'encoded_videos' folder.")
