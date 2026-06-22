# Project 3 Documentation

This folder contains comprehensive guides and documentation for Project 3: DevOps CI/CD Health Monitor.

## 📚 Available Documentation

### [CI/CD Auto-Grading Guide](CI_CD_GUIDE.md)

**Complete guide to the automated testing and grading system**

Learn everything about how your code is automatically tested when you push to GitHub:

- 🔄 **How it works**: Step-by-step explanation of the workflow
- 📊 **Viewing results**: Where to find your scores and test output
- 🚀 **Optimization**: How pip caching speeds up testing
- 🐛 **Troubleshooting**: Common issues and solutions
- 💡 **Best practices**: Development workflow recommendations
- 🔒 **Security**: Understanding private test repositories

**Read this guide if you want to:**
- Understand what happens when you push code
- Learn how to view your test results
- Find out how the auto-grading calculates your score
- Debug workflow failures
- Optimize your development process

---

## 🎯 Quick Links

- **Main README**: [../README.md](../README.md) - Project requirements and implementation guide
- **Workflow File**: [../.github/workflows/autograding.yml](../.github/workflows/autograding.yml) - The actual workflow configuration
- **Token Checker**: [../.github/scripts/check_instructor_token.sh](../.github/scripts/check_instructor_token.sh) - Authentication validation script

---

## 📖 Additional Resources

### For Students

If you're stuck or need more information:

1. **Start with the main README** - Contains all implementation requirements
2. **Review the CI/CD Guide** - Explains automated testing in detail
3. **Check GitHub Actions tab** - View your actual test results
4. **Download artifacts** - Get detailed test output files
5. **Ask for help** - Post in course forum or attend office hours

### For Instructors

Repository setup and configuration:

- Workflow requires `INSTRUCTOR_TESTS_TOKEN` secret configured in repository settings
- Token should have read access to private test repository: `CS3030-master/project3-instructor-tests`
- Students see friendly error message if token not configured

---

*Last Updated: February 9, 2026*
