# XYZ = 866 mod 4 = 2
# Layers = 7
# Heads = 2, 3, 5, 7

out_dir = 'out-shakespeare-char-exam'
eval_interval = 500
eval_iters = 100
log_interval = 10

always_save_checkpoint = True

dataset = 'shakespeare_char'
gradient_accumulation_steps = 1
batch_size = 48
block_size = 256

n_layer = 7
n_head = 7   # change to 2, 3, 5, 7 for different runs
n_embd = 210 # divisible by 2, 3, 5, and 7

dropout = 0.0
bias = False

learning_rate = 1e-3
max_iters = 5000
lr_decay_iters = 5000
min_lr = 1e-4
beta2 = 0.99
warmup_iters = 100

device = 'cuda'
dtype = 'float16'
compile = False