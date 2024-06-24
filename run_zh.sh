# ARG
python main.py \
    --seed 3759 \
    --gpu 3 \
    --lr 2e-5 \
    --model_name ARG \
    --language ch \
    --root_path ./course_data/zh_both_tozero \
    --bert_path "/data/jiayi/ARG/bert-base-uncased" \
    --data_name zh-arg \
    --data_type rationale \
    --rationale_usefulness_evaluator_weight 2.2 \
    --llm_judgment_predictor_weight 1.8 

# # ARG-D abcd dedas if (a < 0) break;
 python main.py \
     --seed 3759 \
     --gpu 3 \
     --lr 5e-4 \
     --model_name ARG-D \
     --language ch \
     --root_path ./course_data/zh_both_tozero \
     --bert_path "/data/jiayi/ARG/bert-base-uncased" \
     --data_name zh-argd \
     --data_type rationale \
     --rationale_usefulness_evaluator_weight 2.2 \
     --llm_judgment_predictor_weight 1.8 \
     --kd_loss_weight 15 \
     --teacher_path ./param_model/ARG_zh-arg/1/parameter_bert.pkl