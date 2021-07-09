!git clone https://github.com/haruyasu/mask-rcnn-custom.git

!git pull

cd mask-rcnn-custom/

!pip install -r requirements.txt

!pip3 uninstall -y keras-nightly
!pip3 uninstall -y tensorflow
!pip3 uninstall -y keras
!pip3 install keras==2.1.6
!pip3 install tensorflow==1.15.0
!pip3 install h5py==2.10.0

cd samples/custom

!python3 custom.py train --dataset=../../dataset --weights=coco

