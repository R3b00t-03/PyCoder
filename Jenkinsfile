pipeline {
    agent none
    stages {
        stage('Build'){
            agent {
                docker {
                    image 'python:3.11.0rc2-windowsservercore-ltsc2022'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m py_compile main.py Generators\\*.py*'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-windows:python3'
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pyinstaller --onefile main.py'
            }
            post {
                success {
                    archiveArtifacts 'dist/main.exe'
                }
            }
        }
    }
}