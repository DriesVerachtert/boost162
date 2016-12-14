#!groovy



node {
	stage('Checkout') {
		checkout scm
	}
	stage('PrintEnv') {
		// workaround: a for each loop doesn't work in Jenkins
		Set keys = this.binding.variables.keySet();
		for (int i = 0; i< keys.size(); i++) {
		  	String key = keys.getAt(i);
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