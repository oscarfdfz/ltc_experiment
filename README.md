# 实验1
先运行实验1再运行实验2，这个比较急
## 切换虚环境
```
cd /home/ltc/generation/Unilm
source ./venv/bin/activate
```
## 1.先运行repo中的data_utils_contrast.py
将data_utils_contrast.py拷贝到/home/ltc/generation/Unilm/unilm/s2s-ft/train_file
在/home/ltc/generation/Unilm/unilm/s2s-ft/train_file目录下运行
```
cd /home/ltc/generation/Unilm/unilm/s2s-ft/train_file
python data_utils_contrast.py
```

## 运行已有的代码，输入以下命令行即可
一、训练：
所在位置/home/ltc/generation/Unilm/unilm/s2s-ft
```
cd /home/ltc/generation/Unilm/unilm/s2s-ft
```
在 /home/ltc/generation/Unilm/unilm/s2s-ft下新建文件夹review_book_output_dir_contrast
```
mkdir review_book_output_dir_contrast
```
运行以下脚本

```
nohup python  run_seq2seq.py   --train_file ./train_file/train1_contrast_trainset.json --output_dir ./review_book_output_dir_contrast   --model_type unilm --model_name_or_path ./model_path/unilm1.2-base-uncased.bin   --do_lower_case  --max_source_seq_length 464 --max_target_seq_length 50   --learning_rate 7e-5 --num_warmup_steps 500 --num_training_steps 16000 --cache_dir ./cache_dir --no_cuda --config_name ./config/unilm1.2-base-uncased-config.json --tokenizer_name /home/ltc/generation/Unilm/unilm/s2s-ft/vocab/unilm1.2-base-uncased-vocab.txt
```

二、进行decode生成
```
nohup python decode_seq2seq.py --model_type unilm --tokenizer_name /home/ltc/generation/Unilm/unilm/s2s-ft/vocab/unilm1.2-base-uncased-vocab.txt --input_file ./train_file/train1_contrast_testset.json --split validation --do_lower_case --model_path /home/ltc/generation/Unilm/unilm/s2s-ft/review_book_output_dir_contrast/ckpt-16000 --config_path /home/ltc/generation/Unilm/unilm/s2s-ft/review_book_output_dir_contrast/ckpt-16000/config.json --max_seq_length 512 --max_tgt_length 50 --batch_size 1 --beam_size 1 --length_penalty 0 --forbid_duplicate_ngrams --mode s2s --forbid_ignore_word "." 
```

三、生成的结果在/home/ltc/generation/Unilm/unilm/s2s-ft/review_book_output_dir_contrast
将生成的文件ckpt-16000.validation给我就好，里面打开应该是很多行文本


# 实验2
## 运行已有的代码，输入以下命令行即可
一、训练：
所在位置/home/ltc/generation/Unilm/unilm/s2s-ft
```
cd /home/ltc/generation/Unilm/unilm/s2s-ft
```
在 /home/ltc/generation/Unilm/unilm/s2s-ft下新建文件夹review_book_output_dir_long
```
mkdir review_book_output_dir_long
```
运行以下脚本
```
nohup python  run_seq2seq.py   --train_file ./train_file/review_book_train1.json --output_dir ./review_book_output_dir_long   --model_type unilm --model_name_or_path ./model_path/unilm1.2-base-uncased.bin   --do_lower_case  --max_source_seq_length 600 --max_target_seq_length 120   --learning_rate 7e-5 --num_warmup_steps 500 --num_training_steps 16000 --cache_dir ./cache_dir --no_cuda --config_name ./config/unilm1.2-base-uncased-config.json --tokenizer_name /home/ltc/generation/Unilm/unilm/s2s-ft/vocab/unilm1.2-base-uncased-vocab.txt
```
二、进行decode生成
```
nohup python decode_seq2seq.py --model_type unilm --tokenizer_name /home/ltc/generation/Unilm/unilm/s2s-ft/vocab/unilm1.2-base-uncased-vocab.txt --input_file ./train_file/review_book_train1_test.json --split validation --do_lower_case --model_path /home/ltc/generation/Unilm/unilm/s2s-ft/review_book_output_dir_long/ckpt-16000 --config_path /home/ltc/generation/Unilm/unilm/s2s-ft/review_book_output_dir_long/ckpt-16000/config.json --max_seq_length 512 --max_tgt_length 100 --batch_size 1 --beam_size 1 --length_penalty 0 --forbid_duplicate_ngrams --mode s2s --forbid_ignore_word "." 
```

三、生成的结果在/home/ltc/generation/Unilm/unilm/s2s-ft/review_book_output_dir_long
将生成的文件ckpt-16000.validation给我就好，里面打开应该是很多行文本

