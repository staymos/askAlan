# askAlan
A chatbot with the personality of Alan Turing designed to pass the Turing Test.

The software  for this tutorial can be downloaded from: https://github.com/tensorflow/nmt
The detailed instructions on how to use this tutorial are contained in the README.md file in that GitHub repository. This appendix lists a summary of the steps to run that tutorial. I had to run this tutorial (or parts of it) several times during the project. I wrote this summary to facilitate doing this so quickly.

Create a Python3 virtualenv.
In Oracle Virtualbox, create an Ubuntu Desktop 16.04 VM, 4GB RAM / 80 GB HDD
In terminal, sudo apt upgrade
sudo apt-get install python3-pip
sudo pip3 install virtualenv

Create a virtualenv for this project.
virtualenv tensorflow
cd tensorflow/
source ./bin/activate

Download code
sudo apt install git
git clone https://github.com/tensorflow/nmt
sudo apt install curl

Download the data:
In my project, I replaced this data with the Q&A dataset, keeping the same filenames.
cd nmt
nmt/scripts/download_iwslt15.sh /tmp/nmt_data
	-train.en
	-train.vi
	-tst2012.en
	-tst2012.vi
	-tst2013.en
	-tst2013.vi
	-vocab.en
	-vocab.vi

Install dependencies needed to run the model
mkdir /tmp/nmt_model
pip install numpy
pip install tensorflow

Run the model
Enter the following command:
python -m nmt.nmt \
    --src=vi --tgt=en \
    --vocab_prefix=/tmp/nmt_data/vocab  \
    --train_prefix=/tmp/nmt_data/train \
    --dev_prefix=/tmp/nmt_data/tst2012  \
    --test_prefix=/tmp/nmt_data/tst2013 \
    --out_dir=/tmp/nmt_model \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=2 \
    --num_units=128 \
    --dropout=0.2 \
    —metrics=bleu

Start Tensorboard to monitor the model build
Open a new terminal window.
tensorboard —logdir=/tmp/nmt_model/
Open a browser:
localhost:6000

To delete the model:

21. cd /tmp/nmt_model
22. rm -r *

To ask the model questions:

23. Open new terminal window
24. Navigate to /tensorflow/nmt
25. Copy askAlan.py into this directory
26. python askAlan.py
