pipeline{
    agent any
    stages{
        stage("Clone the repo"){
            steps{
                git branch: 'main', url:'https://github.com/navyayandapalli/c412jenkins.git'
            }
        }
        stage("Build"){
            steps{
                sh 'javac HelloWorld.java'
            }
        }
        stage("Test"){
            steps{
                sh 'java HelloWorld'
            }
        }
    }
}
