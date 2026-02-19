# 作业调度器

通用配置 json 文件位于：config/json/job_scheduler/xxx.json

## -job

指定作业调度方式：`slurm`、`lsf` 或 `no`。默认为 `no`。

## -lsf_q

使用 LSF 运行。在登录服务器上是必需的。

指定使用 lsf 的 bqueue。例如，python3 run ... -lsf -lsf_q=sim

## -slurm_q

使用 SLURM 运行。在登录服务器上是必需的。

## -slurm_mem

指定 SLURM 中每个任务的内存。默认为 `1000M`。
