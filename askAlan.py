import subprocess

while True:

    print ("\n\n\n")

    q = input("Ask me a Question...  ")

    file = open("/tmp/tstAlan.en","w")
    file.write(q)
    file.close()


    subprocess.run(["python", "-m", "nmt.nmt", 
                "--src=en --tgt=vi", \
                "--vocab_prefix=/tmp/nmt_data/vocab", \
                "--out_dir=/tmp/nmt_model", \
                "--model_dir=/tmp/nmt_model", \
                "--inference_input_file=/tmp/tstAlan.en", \
                "--inference_output_file=/tmp/nmt_model/output_infer"])


    print ("\n\n\n")

    print ("The Question..." + "\n")
    subprocess.run(["cat", "/tmp/tstAlan.en"])

    print ("\n\n")

    print ("The Answer..." + "\n")
    subprocess.run(["cat", "/tmp/nmt_model/output_infer"])

    print ("\n\n\n")
