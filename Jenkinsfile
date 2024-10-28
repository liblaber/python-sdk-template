pipeline {
    agent {        
        label 'ubuntu-latest'
    }
    environment {        
        TWINE_USERNAME = '__token__'  
        TWINE_PASSWORD = credentials('PYPI_TOKEN')  
    }
    stages {
        stage('Run Only on Tag') {
            when {
                expression {
                    
                    return env.BRANCH_NAME ==~ /^rls_\d+\.\d+\.\d+$/  
                }
            }
            steps {
                echo "Running on tag: $env.BRANCH_NAME"
            }
            stages {
                stage('Pre-check for Environment Variables') {
                    steps {
                        script {
                            if (!env.TWINE_PASSWORD) {
                                error("Error: TWINE_PASSWORD is not defined (PYPI_TOKEN missing)")
                            }
                            echo "All necessary environment variables are defined."
                        }
                    }
                }
                stage('Checkout Code') {
                    steps {
                        
                        checkout scm
                    }
                }
                stage('Set up Python') {
                    steps {
                        sh '''
                            sudo apt-get update
                            sudo apt-get install -y python3 python3-pip
                            python3 -m pip install --upgrade pip
                        '''
                    }
                }
                stage('Install Dependencies') {
                    steps {
                        sh '''
                            pip install build twine
                        '''
                    }
                }
                stage('Build and Publish to PyPI') {
                    steps {
                        sh '''
                            python3 -m build
                            twine upload dist/*
                        '''
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()  
        }
    }
}
