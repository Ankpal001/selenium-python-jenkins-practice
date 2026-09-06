pipeline{
 agent any
 stages{
        stage('Test'){steps{bat 'pytest'}}}
 post{
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