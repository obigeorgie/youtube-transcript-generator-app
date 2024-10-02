document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('transcriptForm');
    const result = document.getElementById('result');
    const transcriptContent = document.getElementById('transcriptContent');
    const copyButton = document.getElementById('copyButton');
    const errorDiv = document.getElementById('error');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const videoUrl = document.getElementById('videoUrl').value;
        
        result.classList.add('hidden');
        errorDiv.classList.add('hidden');
        
        try {
            const response = await fetch('/get_transcript', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ url: videoUrl }),
            });
            
            const data = await response.json();
            
            if (response.ok) {
                transcriptContent.textContent = data.transcript;
                result.classList.remove('hidden');
            } else {
                throw new Error(data.error || 'An error occurred while fetching the transcript.');
            }
        } catch (error) {
            errorDiv.textContent = error.message;
            errorDiv.classList.remove('hidden');
        }
    });

    copyButton.addEventListener('click', () => {
        const textArea = document.createElement('textarea');
        textArea.value = transcriptContent.textContent;
        document.body.appendChild(textArea);
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
        
        const originalText = copyButton.textContent;
        copyButton.textContent = 'Copied!';
        copyButton.disabled = true;
        
        setTimeout(() => {
            copyButton.textContent = originalText;
            copyButton.disabled = false;
        }, 2000);
    });
});
