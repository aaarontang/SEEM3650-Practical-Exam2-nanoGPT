from pathlib import Path
import matplotlib.pyplot as plt

# Validation loss at iteration 5000 from the four completed logs
heads = [2, 3, 5, 7]
val_losses = [2.4576, 2.4917, 2.7319, 2.8712]

Path("figures").mkdir(exist_ok=True)

plt.figure(figsize=(6, 4))
plt.plot(heads, val_losses, marker="o")
plt.xlabel("Number of Attention Heads")
plt.ylabel("Validation Loss at Iteration 5000")
plt.title("Architecture Experiment on Shakespeare Dataset")
plt.xticks(heads)
plt.grid(True)
plt.tight_layout()

output_path = "figures/shakespeare_heads_loss.png"
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Saved figure to {output_path}")