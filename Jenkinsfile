pipeline {
  agent any
  
  stages {
    
    
    stage ('Testing Stage') {
       steps {
          withMaven(maven : 'maven_3_6_3') {
            sh 'py -m unittest discover --pattern=test*.py' 
        }
       }
    }
    
    
    

  }
}
