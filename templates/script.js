const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('pdf_file');
const fileInfo = document.getElementById('file-info');
const previewContainer = document.getElementById('preview-container');
const viewBeforeUpload = document.getElementById('viewBeforeUpload');

// Click on upload area triggers file input
uploadArea.addEventListener('click', (e) => {
    if (e.target === uploadArea || e.target.classList.contains('upload-area-text') || e.target.classList.contains('upload-area-icon')) {
        fileInput.click();
    }
});

// Drag and drop support
['dragenter', 'dragover'].forEach(eventName => {
    uploadArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        uploadArea.classList.add('drag-over');
    });
});
['dragleave', 'drop'].forEach(eventName => {
    uploadArea.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        uploadArea.classList.remove('drag-over');
    });
});

uploadArea.addEventListener('drop', (e) => {
    const files = e.dataTransfer.files;
    if (files.length > 0) {
        fileInput.files = files;
        handleFileChange();
    }
});

fileInput.addEventListener('change', handleFileChange);

function updatePreviewVisibility() {
    if (viewBeforeUpload.checked) {
        previewContainer.style.display = '';
    } else {
        previewContainer.style.display = 'none';
    }
}

viewBeforeUpload.addEventListener('change', updatePreviewVisibility);

function handleFileChange() {
    const file = fileInput.files[0];
    fileInfo.textContent = file ? file.name : '';
    previewContainer.innerHTML = '';
    updatePreviewVisibility();
    if (!file || !viewBeforeUpload.checked) return;
    const fileType = file.type;
    if (fileType === 'application/pdf') {
        const fileURL = URL.createObjectURL(file);
        previewContainer.innerHTML = `<embed src="${fileURL}" width="100%" height="400px" type="application/pdf">`;
    } else if (fileType === 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' || file.name.endsWith('.docx')) {
        previewContainer.innerHTML = '<p><b>Preview not supported for Word files. Please proceed to upload.</b></p>';
    } else {
        previewContainer.innerHTML = '<p><b>Preview not available for this file type.</b></p>';
    }
}

// Initial state
updatePreviewVisibility();

document.getElementById('uploadForm').addEventListener('submit', function () {
    document.getElementById('loading').style.display = 'block';
}); 