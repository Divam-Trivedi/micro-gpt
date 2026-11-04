import torch
import torch.nn as nn
import torch.nn.functional as F

# The GPT model is provided for you. It returns raw logits (not probabilities).
# You only need to implement the training loop below.

class Solution:
    def train(self, model: nn.Module, data: torch.Tensor, epochs: int, context_length: int, batch_size: int, lr: float) -> float:
        # Train the GPT model using AdamW and cross_entropy loss.
        # For each epoch: seed with torch.manual_seed(epoch),
        # sample batches from data, run forward/backward, update weights.
        # Return the final loss rounded to 4 decimals.
        loss = None
        optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        for ep in range(epochs):
            torch.manual_seed(ep)
            indices = torch.randint(0, len(data)-context_length, (batch_size, ))
            X_batches = []
            Y_batches = []
            for i in indices:
                X_batches.append(data[i:i+context_length])
                Y_batches.append(data[i+1:i+1+context_length])
            X = torch.stack(X_batches)
            Y = torch.stack(Y_batches)

            logits = model(X)
            logits = logits.view(-1, logits.size(-1))
            Y = Y.view(-1)
            loss = F.cross_entropy(logits, Y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        return round(loss.item(), 4)
            