import type { Profile } from './types';

export const profile: Profile = {
  name: 'WANG Haoxin',
  title: 'Ph.D. Candidate',
  specialties: ['FPGA', 'Detector Electronics', 'High-Speed Data Acquisition', 'Precision Timing'],
  introduction:
    'I develop FPGA-based instrumentation and high-speed data acquisition systems, with research interests in clock recovery, phase uncertainty, and synchronization.',
  currentFocus:
    'Investigating phase uncertainty mechanisms in FPGA high-speed transceivers and developing deterministic multi-channel synchronization techniques.',
  links: [],
  interests: [
    {
      title: 'High-Speed Serial Links',
      description: 'Reliable links with characterized latency, clock recovery, and measurable operating margins.',
      keywords: ['Clock recovery', 'High-speed transceivers', 'Deterministic latency', 'Link characterization'],
    },
    {
      title: 'Precision Timing & Synchronization',
      description: 'Measurement-led methods for repeatable phase behavior across channels and resets.',
      keywords: ['Phase uncertainty', 'Timing calibration', 'Clock synchronization', 'Multi-channel alignment'],
    },
    {
      title: 'FPGA-Based Data Acquisition',
      description: 'Maintainable readout architectures connecting front-end data to high-throughput transport.',
      keywords: ['FPGA', 'DAQ', 'AXI-Stream', 'High-throughput readout', 'RDMA / RoCE'],
    },
  ],
};
