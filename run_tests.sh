
source venv/Scripts/activate

pytest test_app.py

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "One or more tests failed."
    exit 1
fi