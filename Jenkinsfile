pipeline {
    agent any

    environment {
        APPLICATION = 'selenium-python'
    }

    parameters {
        choice(
            name: 'TEST_ENV',
            choices: ['qa', 'staging', 'prod'],
            description: 'Select the test environment'
        )

        choice(
            name: 'BROWSER',
            choices: ['chrome', 'firefox'],
            description: 'Select the browser'
        )
    }

    stages {

        stage('Parallel Tests') {
            parallel {

                stage('Login Tests') {
                    steps {
                        bat 'pytest tests/test_login.py'
                    }
                }

                stage('Negative Tests') {
                    steps {
                        bat 'pytest tests/test_negative_login.py'
                    }
                }
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: false,
                reportDir: 'reports',
                reportFiles: 'pytest-report.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])

            archiveArtifacts(
                artifacts: 'reports/*.html,screenshots/*.png',
                allowEmptyArchive: false
            )
        }

        success {
            echo 'Automation execution PASSED'
        }

        failure {
            echo 'Automation execution FAILED'
        }
    }
}