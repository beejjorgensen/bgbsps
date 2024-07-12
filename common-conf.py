# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_split_index = True

# -- Options for LaTeX output -------------------------------------------------

bgbsps_latex_preamble = r'''
    \usepackage{makeidx}
    \makeindex

    % Custom command to allow different fonts in index entries
    \newcommand{\customindex}[2]{\index{#1@\texttt{#1} #2}}
'''

bgbsps_latex_elements_extra = {}

bgbsps_papersize = os.getenv("BGBSPS_PAPER_SIZE")

if bgbsps_papersize == 'usl':
    bgbsps_papersize = 'letterpaper'
elif bgbsps_papersize == 'a4':
    bgbsps_papersize = 'a4paper'
elif bgbsps_papersize == 'amazon':
    bgbsps_papersize = 'letterpaper'
    bgbsps_latex_elements_extra |= {
        'geometry': r'\usepackage[paperwidth=7.5in,paperheight=9.25in,top=1in,bottom=1in,left=1.25in,right=1.25in]{geometry}',
    }
elif bgbsps_papersize == 'lulu':
    bgbsps_papersize = 'letterpaper'
    bgbsps_latex_elements_extra |= {  # Crown Quatro
        'geometry': r'\usepackage[paperwidth=7.444in,paperheight=9.681in,top=1in,bottom=1in,left=1in,right=1.5in]{geometry}',
    }

bgbsps_sides = os.getenv("BGBSPS_SIDES")

if bgbsps_sides == '1':
    bgbsps_latex_elements_extra |= {
        'extraclassoptions': 'oneside'
    }

bgbsps_color = os.getenv("BGBSPS_COLOR")

if bgbsps_color == 'bw':
    bgbsps_latex_preamble += r'''
        %\sphinxDeclareColorOption{TitleColor}{{gray}{0.25}}
        %\sphinxDeclareColorOption{InnerLinkColor}{{gray}{0.356}}
        %\sphinxDeclareColorOption{OuterLinkColor}{{gray}{0.348}}
        \sphinxDeclareColorOption{TitleColor}{{gray}{0}}
        \sphinxDeclareColorOption{InnerLinkColor}{{gray}{0}}
        \sphinxDeclareColorOption{OuterLinkColor}{{gray}{0}}
        \sphinxDeclareColorOption{VerbatimBorderColor}{{gray}{0.125}}
    '''
    highlight_language = 'none'
    pygments_style = 'none'

latex_engine = 'xelatex'
latex_elements = {
    'preamble': bgbsps_latex_preamble,
    'printindex': r'\printindex',
    'papersize': bgbsps_papersize,
} | bgbsps_latex_elements_extra

# -- Options figure numbering -------------------------------------------------

# Enable figure numbering
numfig = True

# Define the depth of the numbering (usually, chapter is at level 1)
numfig_secnum_depth = 1

# Define the format of the numbering
numfig_format = {
    'figure': 'Figure %s',  # Format for figures
    'table': 'Table %s',  # Format for tables
}

