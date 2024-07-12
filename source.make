SPHINXOPTS ?=
SPHINXBUILD ?= sphinx-build
SOURCEDIR = .
BUILDDIR = build

BGBSPS_DIR ?= ../../bgbsps

TARGETS = html \
    $(GUIDE_ID)_usl_c_2 \
    $(GUIDE_ID)_amazon

.PHONY: all help clean html $(GUIDE_ID)_usl_c_2

all: $(TARGETS)

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean:
	$(SPHINXBUILD) -M clean "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html:
	$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

$(GUIDE_ID)_usl_c_1:
	BGBSPS_PAPER_SIZE=usl \
    BGBSPS_SIDES=1 \
    BGBSPS_COLOR=color \
    $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O)

$(GUIDE_ID)_usl_c_2:
	BGBSPS_PAPER_SIZE=usl \
    BGBSPS_SIDES=2 \
    BGBSPS_COLOR=color \
    $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O)

$(GUIDE_ID)_usl_bw_1:
	BGBSPS_PAPER_SIZE=usl \
    BGBSPS_SIDES=1 \
    BGBSPS_COLOR=bw \
    $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O) -N

$(GUIDE_ID)_usl_bw_2:
	BGBSPS_PAPER_SIZE=usl \
    BGBSPS_SIDES=2 \
    BGBSPS_COLOR=bw \
    $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O) -N

$(GUIDE_ID)_amazon:
	BGBSPS_PAPER_SIZE=amazon \
    BGBSPS_SIDES=2 \
    BGBSPS_COLOR=color \
    $(SPHINXBUILD) -M latexpdf "$(SOURCEDIR)" "$(BUILDDIR)/$@" $(SPHINXOPTS) $(O)
