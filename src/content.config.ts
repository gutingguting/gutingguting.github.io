import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const optionalUrl = z.url().or(z.literal('')).optional();

const projects = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    shortTitle: z.string(),
    date: z.coerce.date(),
    status: z.enum(['Active', 'Ongoing', 'Completed', 'Placeholder']),
    categories: z.array(z.string()),
    tags: z.array(z.string()),
    featured: z.boolean().default(false),
    summary: z.string(),
    role: z.string(),
    metrics: z.array(z.object({ label: z.string(), value: z.string() })).default([]),
    links: z.object({ github: optionalUrl, paper: optionalUrl, slides: optionalUrl }).default({}),
  }),
});

const research = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/research' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    status: z.enum(['Ongoing', 'Planned', 'Completed', 'Placeholder']),
    topics: z.array(z.string()),
    featured: z.boolean().default(false),
  }),
});

const notes = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/notes' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    category: z.enum(['FPGA', 'High-Speed Links', 'DAQ', 'Measurement', 'Statistics']),
    tags: z.array(z.string()),
    published: z.coerce.date(),
    readingTime: z.string(),
    featured: z.boolean().default(false),
    placeholder: z.boolean().default(true),
  }),
});

export const collections = { projects, research, notes };
