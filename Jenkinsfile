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
        stage('Test') {
            options {
                timeout(time: 10, unit: 'MINUTES')
            }

            steps {
                bat 'echo APPLICATION=%APPLICATION%'
                bat 'echo TEST_ENV=%TEST_ENV%'
                bat 'echo BROWSER=%BROWSER%'

                withEnv(['APPLICATION=temporary-app']) {
                    bat 'echo APPLICATION=%APPLICATION%'
                }

                bat 'pytest'
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