for seed in 122 123 124
do
echo "=====Train and evaluate on sider (random split seed=$seed)====="
python ../src/main.py --dataset sider \
        --metric ROC --kernel_type sequence --seed $seed \
        --model_path ../trained_models/sequence_kernel/ \
        --prediction_path ../predictions/sequence_kernel/
echo ""
done