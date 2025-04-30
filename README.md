
# **Video Encoding using PyAV**

Google Drive Link: https://drive.google.com/drive/folders/1ulW5L-blsEDjy-0fee9NfzSRNm6NTuTI?usp=drive_link


## **📌 Key Features**
- **Three Encoding Techniques**:
  - **Only I-frames** (all keyframes)
  - **Single I-frame + P-frames** (predictive frames)
  - **Single I-frame + interleaved P & B-frames** (bi-directional frames)
- **Codec Comparison**: H.264 vs. H.265 vs. AV1 (with golden frames)
- **CRF & QP Analysis**: Impact of different Constant Rate Factor (CRF) and Quantization Parameter (QP) values on file size and quality.
- **GOP Size Variations**: Testing different Group of Pictures (GOP) sizes (15, 30, 150, 250).
- **Static vs. Dynamic Video Analysis**: Compression efficiency for different video types.

---

## **📊 Results Summary**
### **1. H.264 vs. H.265**
- **H.265 (HEVC)** consistently produces **smaller file sizes** at the same CRF compared to H.264.
- **Best for compression**: Interleaved B-frames in H.265 yield the highest savings.

### **2. AV1 with Golden Frames**
- Further improves compression efficiency over H.265.
- Enabled via:
  ```python
  'svtav1-params': 'enable-golden-frame=1',
  'enable-overlays': '1',
  'hierarchical-levels': '4',
  'lookahead': '120'
  ```

### **3. Optimal CRF Range**
- **CRF 18-23** provides the best balance between quality and file size.
- Higher CRF (e.g., 40) significantly reduces size but degrades quality.

### **4. GOP Size Impact**
- **Larger GOP sizes (150, 250)** improve compression for static videos (e.g., surveillance footage).

---

## **🚀 How to Use**
### **1. Install Dependencies**
```bash
pip install av ffmpeg-python
```

### **2. Run Encoding Scripts**
```bash
python scripts/h264_encoding.py --input input_videos/sample.mp4 --crf 23 --gop 15
python scripts/h265_encoding.py --input input_videos/sample.mp4 --crf 18 --gop 30
python scripts/av1_encoding.py --input input_videos/sample.mp4 --crf 22 --enable-golden
```

### **3. Verify Frame Types**
```bash
ffprobe -v error -select_streams v:0 -show_entries frame=pict_type -of csv=print_section=0 output.mp4
```

---

## **📈 Key Takeaways**
- **For best compression**: Use **H.265 with B-frames** or **AV1 with golden frames**.
- **For high quality**: Use **CRF 18-23**.
- **For static videos**: Larger GOP sizes (e.g., 150-250) improve efficiency.

---
Happy encoding! 🎥💻
