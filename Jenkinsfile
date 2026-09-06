pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_ENV',
            choices: ['qa', 'staging', 'prod'],
            description: 'Select the test environment'
        )
    }

    environment {
        BROWSER = 'chrome'
    }

    stages {
        stage('Test') {
            steps {
                bat 'echo TEST_ENV=%TEST_ENV%'
                bat 'echo BROWSER=%BROWSER%'
                bat 'pytest'
            }
        }
    }

    post {
        always {
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'pytest-report.html',
                reportName: 'Pytest HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])
        }
    }
}