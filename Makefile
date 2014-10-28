prepare:
	# install 3X
	[ -x 3x ] || curl -s https://gist.github.com/netj/9065580/raw/get-3x | bash -s release=LATEST dest=.
	# build giraph
	cd giraph && mvn install -DskipTests --projects .,giraph-core
	# build graft
	cd graft && mvn compile
	mkdir -p program/target/
	cp graft/target/*.jar program/target/
	# generate and upload graphs
	$(MAKE) -C graphs
