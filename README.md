# Text-To-Image-On-SageMaker

이 리토는 Text-To-Image 를 위한 SageMaker 에서 Fine-Tuning 및 Pre-Training 에 대한 정보를 담을 예정 입니다.

## Reference
- SageMaker Jumpstart 를 사용하여 미리 훈련된 "model-upscaling-stabilityai-stable-diffusion-x4-upscaler-fp16" 를 배포하여, 기존의 이미지를 추론하여 해상도를 높이는 방법을 설명 합니다.
    - [Jan 2023, Upscale images with Stable Diffusion in Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/upscale-images-with-stable-diffusion-in-amazon-sagemaker-jumpstart/)    
- SageMaker Jumpstart 및 SDK 를 사용하여,Stable Diffusion 2.1 을 모델 배포하고 추론을 합니다. 또한 Transfer Learning 의 Fine-Tuning 을 통하여 스타일을 학습하고 추론을 제공합니다. 
    - [Nov 2022, Generate images from text with the stable diffusion model on Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/generate-images-from-text-with-the-stable-diffusion-model-on-amazon-sagemaker-jumpstart/)
- Stable Diffusion 2.0 이 SageMaker Jumpstart 에서 사용이 가능하다는 블로그 입니다. 
    - [Nov 2022, Stability AI builds foundation models on Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/stability-ai-builds-foundation-models-on-amazon-sagemaker/)
- Diffusers 라이브러리로 Stable Diffusion 을 사용하는 가이드
    - [Aug 2022, Stable Diffusion with 🧨 Diffusers](https://huggingface.co/blog/stable_diffusion)
- SageMaker 에서 10TB 의 데이터를 Stable Diffusion 으로 Pre-Training 블로그
    - [Nov 2022, How I trained 10TB for Stable Diffusion on SageMaker](https://medium.com/@emilywebber/how-i-trained-10tb-for-stable-diffusion-on-sagemaker-39dcea49ce32)