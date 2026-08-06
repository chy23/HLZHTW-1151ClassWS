const fs = require('fs');
let code = fs.readFileSync('src/components/HandoutViewer.jsx', 'utf8');

// Add dark mode classes
code = code.replace(/bg-white/g, 'bg-white dark:bg-slate-800');
code = code.replace(/text-slate-800/g, 'text-slate-800 dark:text-slate-200');
code = code.replace(/text-slate-700/g, 'text-slate-700 dark:text-slate-300');
code = code.replace(/border-slate-100/g, 'border-slate-100 dark:border-slate-700');
code = code.replace(/border-slate-200/g, 'border-slate-200 dark:border-slate-700');
code = code.replace(/bg-slate-50/g, 'bg-slate-50 dark:bg-slate-900');
code = code.replace(/bg-slate-100/g, 'bg-slate-100 dark:bg-slate-700');
code = code.replace(/bg-slate-200/g, 'bg-slate-200 dark:bg-slate-600');
code = code.replace(/text-slate-500/g, 'text-slate-500 dark:text-slate-400');
code = code.replace(/text-slate-600/g, 'text-slate-600 dark:text-slate-300');
code = code.replace(/text-slate-400/g, 'text-slate-400 dark:text-slate-500');
code = code.replace(/text-slate-300/g, 'text-slate-300 dark:text-slate-600');
code = code.replace(/bg-red-50/g, 'bg-red-50 dark:bg-red-900/30');
code = code.replace(/border-red-300/g, 'border-red-300 dark:border-red-800');

// Header icons and buttons
code = code.replace("import { PenTool, Eraser, Trash2, ZoomIn, ZoomOut, Menu } from 'lucide-react';", 
"import { PenTool, Eraser, Trash2, Menu, Moon, Sun, Brush, Type, Eye, EyeOff } from 'lucide-react';");

fs.writeFileSync('src/components/HandoutViewer.jsx', code);
console.log("Transformed HandoutViewer");
