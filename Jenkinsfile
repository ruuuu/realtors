pipeline {
  agent any
  
  stages {
    
    
    stage ('Testing Stage') {
       steps {
          withMaven(maven : 'maven_3_6_3') {
            sh 'python3 -m pytest' 
        }
       }
    }
    
    
    

  }
}
