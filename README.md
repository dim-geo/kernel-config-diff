# kernel-config-diff
Diff kernel configs but keep the structure for easier comparison

When kernel configs are diffed it's hard to view the tree structure of kenrel config.
/scripts/diffconfig from kernel does not preserve tree structure as well.

This tool aims to alleviate that:
 2 kernels configs are parsed and CONFIG_ vairables are stored in a tree (https://anytree.readthedocs.io/en/latest/) structure based on # comments that do not have CONFIG_.
 Then CONFIG_ that have the same common value are removed from both trees.
 Finally, pruned trees are saved in txt files for easier diff-ing with GUI tools like meld. This will help you easily spot the differences and the place of xconfig, menuconfig that you can change them.

 Usage:
 `kernel-config-diff.py oldconfig newconfig oldtree.txt newtree.txt`
 
 Sample output of a tree:
 
 ```
 ./current_config
+- Automatically generated file; DO NOT EDIT.
   +- Linux/x86 6.1.27 Kernel Configuration
      |- CONFIG_CC_VERSION_TEXT:"gcc"
      |- CONFIG_GCC_VERSION:120201
      |- CONFIG_PAHOLE_VERSION:0
      |- General setup
      |  |- CONFIG_LOCALVERSION:"-x86_64"
      |  |- CONFIG_LOCALVERSION_AUTO:is not set
      |  |- CONFIG_KERNEL_LZ4:y
      |  |- CONFIG_KERNEL_ZSTD:is not set
      |  |- CONFIG_DEFAULT_HOSTNAME:"(none)"
      |  |- CONFIG_USELIB:y
      |  |- IRQ subsystem
      |  |- Timers subsystem
      |  |- BPF subsystem
      |  |- CPU/Task time and stats accounting
      |  |- RCU Subsystem
      |  |  +- CONFIG_FORCE_TASKS_TRACE_RCU:is not set
      |  |- CONFIG_PRINTK_INDEX:is not set
      |  |- Scheduler features
      |  |- CONFIG_GCC11_NO_ARRAY_BOUNDS:y
      |  |- CONFIG_SCHED_BORE:y
      |  |- CONFIG_SCHED_AUTOGROUP:is not set
      |  |- CONFIG_CC_OPTIMIZE_FOR_PERFORMANCE:y
      |  |- CONFIG_EXPERT:y
      |  |- CONFIG_DEBUG_RSEQ:is not set
      |  |- CONFIG_PC104:y
      |  +- Kernel Performance Events And Counters
      |- Processor type and features
      |  |- CONFIG_X86_EXTENDED_PLATFORM:y
      |  |- CONFIG_X86_NUMACHIP:y
      |  |- CONFIG_X86_VSMP:is not set
      |  |- CONFIG_X86_UV:is not set
      |  |- CONFIG_X86_GOLDFISH:is not set
      |  |- CONFIG_X86_INTEL_MID:is not set
      |  |- CONFIG_IOSF_MBI_DEBUG:y
      |  |- CONFIG_PARAVIRT_TIME_ACCOUNTING:is not set
      |  |- CONFIG_GENERIC_CPU:is not set
      |  |- CONFIG_MNATIVE_INTEL:y
      |  |- CONFIG_X86_INTEL_USERCOPY:y
      |  |- CONFIG_X86_USE_PPRO_CHECKSUM:y
      |  |- CONFIG_X86_P6_NOP:y
      |  |- CONFIG_PROCESSOR_SELECT:y
      |  |- CONFIG_GART_IOMMU:y
      |  |- CONFIG_NR_CPUS:64
      |  |- CONFIG_X86_MCELOG_LEGACY:y
      |  |- Performance monitoring
      |  |  |- CONFIG_PERF_EVENTS_INTEL_UNCORE:y
      |  |  |- CONFIG_PERF_EVENTS_AMD_POWER:is not set
      |  |  +- CONFIG_PERF_EVENTS_AMD_BRS:is not set
      |  |- CONFIG_X86_PMEM_LEGACY:y
      |  |- CONFIG_MTRR_SANITIZER_SPARE_REG_NR_DEFAULT:1
      |  |- CONFIG_X86_INTEL_TSX_MODE_ON:y
      |  |- CONFIG_X86_INTEL_TSX_MODE_AUTO:is not set
      |  |- CONFIG_HZ_300:is not set
      |  |- CONFIG_HZ_500:y
      |  +- CONFIG_HZ:500
      |- Power management and ACPI options
...
 ```
