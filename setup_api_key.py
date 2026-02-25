"""
API Key Setup Helper
This script helps you set up a new Gemini API key after the old one was compromised.
"""

import os
from pathlib import Path

print("="*70)
print("🔐 GEMINI API KEY SETUP HELPER")
print("="*70)

print("\n⚠️  YOUR CURRENT API KEY HAS BEEN COMPROMISED")
print("\nThis happened because:")
print("  • The API key was exposed in version control")
print("  • Google automatically detects and disables leaked keys")
print("  • This is a security feature to protect you")

print("\n" + "="*70)
print("📝 HOW TO GET A NEW API KEY")
print("="*70)

print("\nStep 1: Visit Google AI Studio")
print("  🌐 URL: https://makersuite.google.com/app/apikey")
print("  (or: https://aistudio.google.com/app/apikey)")

print("\nStep 2: Sign in with your Google Account")
print("  • Use the same account or create a new one")
print("  • It's free to use")

print("\nStep 3: Create a new API key")
print("  • Click 'Create API Key' button")
print("  • Choose 'Create API key in new project' or select existing project")
print("  • Copy the API key that's generated")

print("\nStep 4: Update your .env file")
env_file = Path(__file__).parent / ".env"
print(f"  📁 Location: {env_file}")
print("\n  Open the .env file and replace the line:")
print("  GEMINI_API_KEY=AIzaSyBcIUj_u6KUZ_H5Yw63FF2YFwxIuqxHsIo")
print("\n  With:")
print("  GEMINI_API_KEY=your_new_api_key_here")

print("\nStep 5: IMPORTANT - Secure your API key")
print("  ⚠️  NEVER commit .env file to version control!")
print("  ⚠️  NEVER share your API key publicly!")
print("  ⚠️  Add .env to .gitignore if using Git")

print("\nStep 6: Restart the application")
print("  python main.py")

print("\n" + "="*70)
print("🔒 SECURITY BEST PRACTICES")
print("="*70)

print("\n1. Keep .env file local only")
print("   • Never commit to Git/GitHub")
print("   • Add to .gitignore")

print("\n2. Use environment variables in production")
print("   • Set system environment variables")
print("   • Use secrets management services")

print("\n3. Rotate API keys regularly")
print("   • Change keys every few months")
print("   • Delete old unused keys")

print("\n4. Monitor API usage")
print("   • Check Google Cloud Console")
print("   • Set up usage alerts")

print("\n" + "="*70)
print("📋 QUICK CHECKLIST")
print("="*70)

checklist = [
    ("Visit https://makersuite.google.com/app/apikey", False),
    ("Create new API key", False),
    ("Copy the new API key", False),
    ("Open .env file in text editor", False),
    ("Replace old GEMINI_API_KEY value", False),
    ("Save .env file", False),
    ("Verify .env is in .gitignore", False),
    ("Restart application", False)
]

for i, (task, done) in enumerate(checklist, 1):
    status = "✅" if done else "☐"
    print(f"  {status} {i}. {task}")

print("\n" + "="*70)
print("🆘 NEED HELP?")
print("="*70)

print("\nCommon Issues:")
print("\n1. Can't access Google AI Studio")
print("   → Try: https://aistudio.google.com/app/apikey")
print("   → Or: https://console.cloud.google.com/")

print("\n2. API key still not working")
print("   → Wait 1-2 minutes after creating")
print("   → Check for extra spaces in .env file")
print("   → Ensure no quotes around the API key")

print("\n3. .env file format")
print("   Correct format:")
print("   GEMINI_API_KEY=AIzaSyD...")
print("   NOT: GEMINI_API_KEY='AIzaSyD...'")
print("   NOT: GEMINI_API_KEY=\"AIzaSyD...\"")

print("\n" + "="*70)
print("✅ AFTER SETUP")
print("="*70)

print("\nRun this to verify:")
print("  python verify_fixes.py")

print("\nThen launch the application:")
print("  python main.py")

print("\n" + "="*70)
print("🔗 USEFUL LINKS")
print("="*70)

print("\n• Google AI Studio: https://makersuite.google.com/app/apikey")
print("• Gemini API Docs: https://ai.google.dev/docs")
print("• API Key Management: https://console.cloud.google.com/apis/credentials")
print("• .gitignore Guide: https://git-scm.com/docs/gitignore")

print("\n" + "="*70)

# Try to check if .gitignore exists and has .env
gitignore_file = Path(__file__).parent / ".gitignore"
if gitignore_file.exists():
    with open(gitignore_file, 'r') as f:
        content = f.read()
        if '.env' in content:
            print("✅ Good: .env is in .gitignore")
        else:
            print("⚠️  WARNING: .env is NOT in .gitignore!")
            print("   Add this line to .gitignore:")
            print("   .env")
else:
    print("⚠️  WARNING: No .gitignore file found!")
    print("   Create .gitignore and add:")
    print("   .env")
    print("   *.pyc")
    print("   __pycache__/")

print("="*70)
print("\n💡 Ready to get started? Follow the steps above!")
print("\n")
