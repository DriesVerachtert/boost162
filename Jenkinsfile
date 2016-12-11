#!groovy



node {
	stage('Checkout') {
		checkout scm
	}
	stage('PrintEnv') {
		this.binding.variables.each {k,v -> println "$k = $v"}

		sh 'env | sort'
	}

	stage('CopySources') {

	}
	stage('BuildUntested') {
		//sh "sudo /srv/rpmbuild/scripts/run-single-scl-build-from-jenkins.pl "
	}
}