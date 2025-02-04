
# 🧠 Brain Tumor Diagnosis using Deep Learning  

## 📝 Project Overview  
An AI-powered deep learning model for **automated brain tumor detection, classification, and localization** using MRI scans, leveraging CNN, U-Net, ResNet50, and VGG19 for **highly accurate diagnosis**.  

## 🚀 Introduction  
Brain tumor diagnosis is **critical yet challenging** with traditional manual methods. This project uses **deep learning** to **automate, expedite, and enhance accuracy** in tumor classification, reducing human error and improving patient outcomes.  

🔹 **Models Used:** CNN, U-Net, ResNet50, VGG19  
🔹 **Dataset:** 7,022 MRI scans of Glioma, Meningioma, Pituitary Tumors, and No Tumor cases  
🔹 **Best Accuracy:** VGG19 (99.65%)  
🔹 **Key Features:** Automated diagnosis, improved scalability, real-time processing  

## 🛠️ User Instructions  

### 📌 Installation  
1. **Clone the Repository**  
   ```bash
   git clone --branch 8f82fb52288bada5f1efda948b9c4c414a131c1f https://github.com/ajaychary06/projects.git

   cd projects/Deep-learning-for-automated-brain-tumor-diagnosis-in-MRI-scans
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Run the Model**
	 ```bash 
   python main.py
   
4. **Upload MRI Scan & Get Prediction**
   
	🔹 The system will classify the MRI scan into one of the four tumor types.

	🔹 View results in terminal or visualization panel.

# 👨‍💻 Developer Instructions
##  🔧 How to Build and Install
1. **Set up a Virtual Environment (Recommended)**
	``` bash
	python -m venv env
	source env/bin/activate  # On Windows use: env\Scripts\activate
2. **Install Required Libraries**
	```bash
	pip install -r requirements.txt
3. **Train the Model (Optional)**
   ```bash
   python train.py --model vgg19 --epochs 10
4. **Test the Model**
	```bash
 	python test.py
5. **Deploy as an API (FastAPI Example)**
	```bash
 	uvicorn app:app --host 0.0.0.0 --port 8000
6. **Run on Jupyter Notebook (For Experimentation)**
   ```bash
   jupyter notebook

# 🎯 What to Expect

✔ Accurate Predictions - Classification of MRI scans with high precision.

✔ User-Friendly Execution - Simple CLI and API-based model interaction.

✔ Scalability - Can be integrated into healthcare systems for automated diagnosis.

✔ Room for Improvements - Open for contributions to enhance model performance

### 📢 Contributions & Feedback are welcome! Feel free to fork, improve, and create PRs.

#### 🔗 Connect 

For questions or collaboration, feel free to reach out to [www.linkedin.com/in/ajaychary-kandukuri-053a5a25a]







