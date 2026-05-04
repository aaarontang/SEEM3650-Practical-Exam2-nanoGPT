out_dir = 'out-code-generation'
eval_interval = 500
eval_iters = 100
log_interval = 10

always_save_checkpoint = True

dataset = 'code_generation'
gradient_accumulation_steps = 1
batch_size = 32
block_size = 256

n_layer = 6
n_head = 6
n_embd = 384

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