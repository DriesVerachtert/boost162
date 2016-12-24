#!groovy


@NonCPS def printEnv(vars) {
	// workaround: a for each loop doesn't work in Jenkins
	Set keys = vars.keySet();
	for (int i = 0; i< keys.size(); i++) {
	  	String key = keys.getAt(i);
	    println("key: " + key + ", val: " + vars.get(key));                             
	}

}


node {
	stage('Checkout') {
		checkout scm
	}
	stage('PrintEnv') {
		printEnv(this.binding.variables)
		sh 'env | sort'
	}

	stage('BuildUntested') {
		sh "sudo /srv/rpmbuild/scripts/run-single-scl-build-from-jenkins.pl boost162 centos-7-x86_64-scl-untested el7 dries-scl-boost162-centos-7-x68_64"
	}
}
