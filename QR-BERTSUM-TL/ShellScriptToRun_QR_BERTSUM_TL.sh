export BERT_DATA_PATH="/Debatepedia_Dataset_bert/"
export MODEL_PATH="/model_QR-BETSUM-TL_from_XSUM/"
mkdir -p -- "$MODEL_PATH"
export PRE_CKPT="/bertsumextabs_xsum_final_model/model_step_30000.pt"
python "/QR-BERTSUM-TL/src/train.py"  -task abs -mode train -bert_data_path $BERT_DATA_PATH -dec_dropout 0.2  -model_path $MODEL_PATH -sep_optim true -lr_bert 0.002 -lr_dec 0.2 -save_checkpoint_steps 30000 -batch_size 500 -train_steps 60000 -report_every 30000 -accum_count 5 -use_bert_emb true -use_interval true -warmup_steps_bert 6000 -warmup_steps_dec 2000 -max_pos 100 -visible_gpus 0,1,2,3 -log_file "/logs/dp.log" -train_from $PRE_CKPT

