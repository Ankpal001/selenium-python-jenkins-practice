pipeline {
    agent none

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
                    agent {
                        label 'windows-selenium'
                    }

                    options {
                        timeout(time: 5, unit: 'MINUTES')
                    }

                    steps {
                        retry(2) {
                            bat 'pytest tests/test_login.py --html=reports/login-report.html --self-contained-html'
                        }
                    }
                }

                stage('Negative Tests') {
                    agent {
                        label 'windows-selenium'
                    }

                    options {
                        timeout(time: 5, unit: 'MINUTES')
                    }

                    steps {
                        retry(2) {
                            bat 'pytest tests/test_negative_login.py --html=reports/negative-report.html --self-contained-html'
                        }
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
                reportFiles: 'login-report.html',
                reportName: 'Login Test Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])

            publishHTML([
                allowMissing: false,
                reportDir: 'reports',
                reportFiles: 'negative-report.html',
                reportName: 'Negative Test Report',
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