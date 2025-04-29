import { defineConfig, devices } from '@playwright/test';
require('dotenv').config()
import { platform } from 'os';

const isWindows = platform() === 'win32';
const isCI = !!process.env.CI;

// console.log(process.env) // remove this after you've confirmed it is working
/**
 * Read environment variables from file.
 * https://github.com/motdotla/dotenv
 */
// require('dotenv').config();

/**
 * See https://playwright.dev/docs/test-configuration.
 */
export default defineConfig({
  testDir: './tests',
  /* Run tests in files in parallel */
  fullyParallel: false,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  /* Opt out of parallel tests on CI. */
  workers: 1,
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: [
    ['html', { open: 'never' }],
    ['dot'],
    ['json', { outputFile: 'summary.json' }],
  ],
  /* Shared settings for all the projects below. See https://playwright.dev/docs/api/class-testoptions. */
  use: {
    /* Base URL to use in actions like `await page.goto('/')`. */
    // baseURL: 'http://127.0.0.1:3000',

    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: 'retain-on-failure',
    video: 'retain-on-failure',
    launchOptions: { slowMo: 1500},
    ignoreHTTPSErrors: true
    
    
  },

  webServer: {
    command: process.env.CI
      // CI command: Create venv, install dependencies, and run app
      ? 'cd .. && python -m venv venv && ' + 
        (isWindows 
          // Windows CI environment (Azure Pipelines)
          ? 'venv\/Scripts\/pip.exe install -r requirements.txt && venv\/Scripts\/python.exe app.py'  
          // Linux/macOS CI environment 
          : './venv/bin/pip install -r requirements.txt && ./venv/bin/python app.py')
      // Local command
      : isWindows
        ? 'cd .. && powershell -Command ". .\/venv\/Scripts\/Activate.ps1; python app.py"'
        : 'cd .. && source venv/bin/activate && python app.py',
    url: 'http://localhost:5000',
    reuseExistingServer: !isCI,
    stdout: 'pipe',
    stderr: 'pipe',
    timeout: 30000, // Increased timeout to 30 seconds for CI environments
  },

  timeout: 180000,
  expect: {timeout: 15000},

  /* Configure projects for major browsers */
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'],
      viewport:{width:1920, height:1080}, headless:true },
    },

  

    // {
    //   name: 'firefox',
    //   use: { ...devices['Desktop Firefox'] },
    // },

    // {
    //   name: 'webkit',
    //   use: { ...devices['Desktop Safari'] },
    // },

    /* Test against mobile viewports. */
    // {
    //   name: 'Mobile Chrome',
    //   use: { ...devices['Pixel 5'] },
    // },
    // {
    //   name: 'Mobile Safari',
    //   use: { ...devices['iPhone 12'] },
    // },

    /* Test against branded browsers. */
    // {
    //   name: 'Microsoft Edge',
    //   use: { ...devices['Desktop Edge'], channel: 'msedge' },
    // },
    // {
    //   name: 'Google Chrome',
    //   use: { ...devices['Desktop Chrome'], channel: 'chrome' },
    // },
  ],

  /* Run your local dev server before starting the tests */
  // webServer: {
  //   command: 'npm run start',
  //   url: 'http://127.0.0.1:3000',
  //   reuseExistingServer: !process.env.CI,
  // },
});
