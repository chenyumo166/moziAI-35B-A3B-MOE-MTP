#!/usr/bin/env python3
"""Build Ollama Go template and Modelfile for MoziAI-35B V3.7"""
import os

OUT_DIR = r"F:\fin_moe\dist\moziAI-35B\V3.7"

# --- 1. Write Go template ---
GOTMPL = os.path.join(OUT_DIR, "moziAI-V3.7-35B-chat-template-ollama.gotmpl")

lines = []
a = lines.append

# Tool block
a('{{- if .Tools }}')
a('<|im_start|>system')
a('# Tools')
a('')
a('You have access to the following functions:')
a('')
a('<tools>')
a('{{- range .Tools }}')
a('{{ . }}')
a('{{- end }}')
a('</tools>')
a('')
a('If you choose to call a function ONLY reply in the following format with NO suffix:')
a('')
a('<tool_call>')
a('<function=example_function_name>')
a('<parameter=example_parameter_1>')
a('value_1')
a('