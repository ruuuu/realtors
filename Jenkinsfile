pipeline {
  agent any
  
  stages {
    stage ('Compile Stage') {
      
      steps {
        withMaven(maven : 'maven_3_6_3') {
            sh ''
        }
      }
    }
    
    stage ('Testing Stage') {
       steps {
          withMaven(maven : 'maven_3_6_3') {
            sh 'python3 -m pytest' 
        }
       }
    }
    
    
    stage ('Deployment Stage'){
      steps {
        withMaven(maven : 'maven_3_6_3') {
            sh 'python py test' //подправить
      }
    }
  
  }
 

  }
}
