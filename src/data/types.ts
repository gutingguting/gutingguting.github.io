export interface ExternalLink {
  label: string;
  href: string;
}

export interface ResearchInterest {
  title: string;
  description: string;
  keywords: string[];
}

export interface Profile {
  name: string;
  title: string;
  specialties: string[];
  introduction: string;
  currentFocus: string;
  location?: string;
  links: ExternalLink[];
  interests: ResearchInterest[];
}

export interface Education {
  period: string;
  degree: string;
  institution: string;
  detail?: string;
}

export interface SkillGroup {
  title: string;
  skills: string[];
}

export interface Publication {
  id: string;
  year: number;
  title: string;
  authors: string[];
  venue: string;
  type: 'journal' | 'conference' | 'preprint' | 'talk' | 'poster' | 'report';
  doi?: string;
  pdf?: string;
  code?: string;
  slides?: string;
  featured?: boolean;
  placeholder?: boolean;
}
