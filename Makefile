NULL=

REPO=https://github.com/elmarco/ironrdp-fedora/

IRONRDP_CRATES=\
	       error \
	       core \
	       pdu \
	       graphics \
	       input \
	       svc \
	       dvc \
	       connector \
	       async \
	       displaycontrol \
	       session \
	       cliprdr \
	       rdpdr \
	       rdpsnd \
	       acceptor \
	       ainput \
	       tokio \
	       server \
	       blocking \
	       cliprdr-native \
	       $(NULL)

update:
	for c in $(IRONRDP_CRATES); do \
	 (cd rust-ironrdp-$$c && rust2rpm -s) \
	done

coprbuild:
	for c in $(IRONRDP_CRATES); do \
	 (copr buildscm qemu-rdp --clone-url $(REPO) --subdir rust-ironrdp-$$c) \
	done

print-%:
	@echo '$*=$($*)'
