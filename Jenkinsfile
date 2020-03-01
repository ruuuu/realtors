pipeline {
  agent any
  stages {
     stage('build') {
            steps {
                
                sh 'pip install -r requirements.txt'
            }
        }
     stage('test') {
      steps {
        sh 'nosetests test_create_obuavleune.py'
      }   
    }
  }
}
