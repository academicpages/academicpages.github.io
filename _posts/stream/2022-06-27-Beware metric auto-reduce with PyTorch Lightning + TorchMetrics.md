---
date: 2022-06-27
tags:
- stream
- python
- nn
title: Beware metric auto-reduce with PyTorch Lightning + TorchMetrics
---

PyTorch Lightning + TorchMetrics can log metrics per step and per epoch. It also has `MetricCollection`, which can be used to compute several metrics at once, getting rid of redundant code. Here is how I have it set up:

```python
class BaseModule(pl.LightningModule):
    def __init__(self):
        self.train_metrics = torchmetrics.MetricCollection(
            [
                torchmetrics.Accuracy(),
                torchmetrics.Precision(),
                torchmetrics.Recall(),
                torchmetrics.F1Score(),
            ]
        )

    def training_step(self, batch, batch_idx):
        label = self.get_label(batch)
        out = self.forward(batch)
        loss = self.loss_fn(out, label)
        
        output = self.train_metrics(out, label.int())
        self.log_dict(output, on_step=False, on_epoch=True)
        return loss
```

This code works for Accuracy, but it computes the wrong value for for Precision, Recall, and F1Score. To calculate each metric's value `on_epoch`, PyTorch Lightning averages[^1] the values logged for each batch, weighted by the batch size. This gives the incorrect value for e.g. F1Score.

The docs state that "If `on_epoch` is True, the logger automatically logs the end of epoch metric value by calling `.compute()`." [^2] Maybe because I was using `self.log_dict` instead of `self.log`, this does not have the same effect.

To fix it, I changed my code in this way:

```diff
 class BaseModule(pl.LightningModule):
     def __init__(self):
         self.train_metrics = torchmetrics.MetricCollection(
             [
                 torchmetrics.Accuracy(),
                 torchmetrics.Precision(),
                 torchmetrics.Recall(),
                 torchmetrics.F1Score(),
             ]
         )
 
     def training_step(self, batch, batch_idx):
         label = self.get_label(batch)
         out = self.forward(batch)
         loss = self.loss_fn(out, label)
         
-        output = self.train_metrics(out, label.int())
-        self.log_dict(output, on_step=False, on_epoch=True)
+        self.train_metrics.update(out, label.int())
         return loss
+    
+    def training_epoch_end(self, outputs):
+        self.log_dict(self.train_metrics.compute(), on_step=False, on_epoch=True)
+        self.train_metrics.reset()
```

This code explicitly calls `Metric.update()` and `Metric.compute()` to compute the metric how God intended it. Yeehaw.

[^1]:  by default, but other reducers can be used
[^2]:  [TorchMetrics in PyTorch Lightning — PyTorch-Metrics 0.9.1 documentation](https://torchmetrics.readthedocs.io/en/stable/pages/lightning.html?highlight=on_epoch#logging-torchmetrics)