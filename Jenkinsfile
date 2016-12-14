#!groovy



node {
	stage('Checkout') {
		checkout scm
	}
	stage('PrintEnv') {
		for (String key: this.binding.variables.keySet()) {
			println("key: " + key + ", val: " + this.binding.variables.get(key));
		}

		sh 'env | sort'
	}

	stage('CopySources') {

	}
	stage('BuildUntested') {
		//sh "sudo /srv/rpmbuild/scripts/run-single-scl-build-from-jenkins.pl "
	}
}