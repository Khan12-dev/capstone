pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Starting Capstone Pipeline...'
            }
        }

        stage('Run Parallel Tests') {
            steps {
                bat '"C:\\Users\\SPARTA\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" -m pytest -n 2 -v --html=report.html --self-contained-html'
            }
        }
    }

    post {
        always {
            publishHTML([
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Capstone Test Report'
            ])
        }

        success {
            echo 'Build PASSED - Ready for Deployment!'

            emailext(
                subject: "PASS: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                body: """<p>Good news! Build PASSED.</p>
<p>Job: ${env.JOB_NAME}</p>
<p>Build Number: ${env.BUILD_NUMBER}</p>
<p>Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                to: "umerkhan2211e@gmail.com",
                mimeType: 'text/html'
            )
        }

        failure {
            echo 'Build FAILED - Check Report!'

            emailext(
                subject: "FAIL: ${env.JOB_NAME} - Build #${env.BUILD_NUMBER}",
                body: """<p>Build FAILED - Please check.</p>
<p>Job: ${env.JOB_NAME}</p>
<p>Build Number: ${env.BUILD_NUMBER}</p>
<p>Build URL: <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>""",
                to: "umerkhan2211e@gmail.com",
                mimeType: 'text/html',
                attachmentsPattern: 'report.html'
            )
        }
    }
}
